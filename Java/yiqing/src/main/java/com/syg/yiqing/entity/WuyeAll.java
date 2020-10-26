package com.syg.yiqing.entity;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "wuye_all")
public class WuyeAll {

    @Id // 该字段对应数据库中的列为主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 主键自增长
    @Column(name = "id") // 对应tradition_office表中的id列
    private Integer id;

    @Column(name = "name")
    private String name;

    @Column(name = "legal_person")
    private String legal_person;

    @Column(name = "phone")
    private String phone;

    @Column(name = "province")
    private String province;

    @Column(name = "city")
    private String city;

    @Column(name = "address")
    private String address;

    @Column(name = "email")
    private String email;

    @Column(name = "website")
    private String website;



}
