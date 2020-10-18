package com.syg.yiqing.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.awt.*;
import java.sql.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "future_room")
public class FutureRoom {
    @Id // 该字段对应数据库中的列为主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 主键自增长
    @Column(name = "id") // 对应tradition_office表中的id列
    private Integer id;

    @Column(name = "name")
    private String name;

    @Column(name = "tags")
    private String tags;

    @Column(name = "address")
    private String address;

    @Column(name = "opening_date")
    private Date opening_date;

    @Column(name = "city")
    private String city;

    @Column(name = "url")
    private String url;

}
