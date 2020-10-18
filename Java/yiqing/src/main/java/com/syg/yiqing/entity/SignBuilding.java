package com.syg.yiqing.entity;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.awt.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Entity
@Table(name = "sign_building")
public class SignBuilding {

    @Id // 该字段对应数据库中的列为主键
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 主键自增长
    @Column(name = "id") // 对应tradition_office表中的id列
    private Integer id;

    @Column(name = "name")
    private String name;

    @Column(name = "address")
    private String address;

    @Column(name = "height")
    private String height;

    @Column(name = "wall_type")
    private String wall_type;

    @Column(name = "wall_area")
    private String wall_area;

    @Column(name = "href")
    private String href;

}
